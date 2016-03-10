#include <gazebo/gazebo.h>

namespace gazebo
{
	class BasicModelPlugin : public ModelPlugin
	{
	public: void Load(physics::ModelPtr _parent, sdf::ElementPtr)
		{
			this->model = _parent;

			this->updateConnection = event::Events::ConnectWorldUpdateBegin(
				boost::bind(&ModelPush::OnUpdate,this,_1));
		}


	//called whenever the World calls its update method
	public: void OnUpdate(const common::UpdateInfo &)
	{
		this->model->SetLinearVel(math::Vector3(.03,0,0));
	}

	//pointer to the model
	private: physics::ModelPtr model;

	private: event::ConnectionPtr updateConnection;
	};

	GZ_REGISTER_MODEL_PLUGIN(ModelPush);
}